# server-based syntax
# ======================
# Defines a single server with a list of roles and multiple properties.
# You can define all roles on a single server, or split them:

# server "example.com", user: "deploy", roles: %w{app db web}, my_property: :my_value
# server "example.com", user: "deploy", roles: %w{app web}, other_property: :other_value
# server "db.example.com", user: "deploy", roles: %w{db}
require 'json'

server "srvz-webapp.he-arc.ch", user: "poweruser", roles: %w{app db web}, port:1447

set :deploy_to, "/var/www/#{fetch(:application)}"

namespace :uwsgi do
    desc 'Restart application'
    task :restart do
        on roles(:web) do |h|
	        execute :sudo, 'sv reload uwsgi'
	    end
    end
end

namespace :python do
    def venv_path
        File.join(shared_path, 'env')
    end

    desc 'Create venv'
    task :create_venv do
        on roles([:app, :web]) do |h|
	        execute "python3 -m venv #{venv_path}"
            execute "source #{venv_path}/bin/activate"
	        execute "#{venv_path}/bin/pip install -r #{release_path}/backend/requirements.txt"
        end
    end

    desc 'Config file environement'
    task :django_config do
        on roles([:app, :web]) do |h|
            def config_path
                File.join(shared_path, 'config/env.py')
            end

            def upload_src_path
                File.join(shared_path, "uploads")
            end

            def upload_target_path
                File.join(release_path, "backend/#{fetch(:projectname)}/uploads")
            end

            def target_path
                File.join(release_path, "backend/#{fetch(:projectname)}/#{fetch(:projectname)}/env.py")
            end

            info "config file #{config_path}"
            if test("[ -f #{config_path} ]")
                info "Env config file found"
                
                if test("[ -f #{target_path} ]")
                    info "Remove old sym link"
                    execute "rm #{target_path}"
                end
                info "Creating symlink"
                execute "ln -s #{config_path} #{target_path}"
            end
            
            info "Setup upload symlink"
            execute "ln -s #{upload_src_path} #{upload_target_path}"

        end
    end


    desc 'Django Migrations'
    task :django_migration do
        on roles([:app, :web]) do |h|
	    execute "#{venv_path}/bin/python #{release_path}/backend/guideme/manage.py migrate"
        end
    end
end

namespace :npm do
    def front_path
        File.join(release_path, 'frontend')
    end

    desc 'NPM install dependencies'
    task :install do
        on roles(:web) do
            execute "cd '#{front_path}'; mv .env.json.example .env.json; npm install"
        end
    end

    desc 'VueJs build app'
    task :build do
        on roles(:web) do |h|
            execute "cd '#{front_path}'; npm run build"
        end
    end
end

after 'deploy:publishing', 'uwsgi:restart'
after 'deploy:updating', 'python:create_venv'
after 'python:create_venv', 'python:django_config'
after 'python:django_config', 'python:django_migration'
after 'python:django_migration', 'npm:install'
after 'npm:install', 'npm:build'


# def createJsonFile
#     env_file = {
#         "client_id" => "0",
#         "client_secret" => "0"
#     }
#     File.open("/.env.json", "w") do |f|
#         f.write(env_file.to_json)
#     end
# end