# server-based syntax
# ======================
# Defines a single server with a list of roles and multiple properties.
# You can define all roles on a single server, or split them:

# server "example.com", user: "deploy", roles: %w{app db web}, my_property: :my_value
# server "example.com", user: "deploy", roles: %w{app web}, other_property: :other_value
# server "db.example.com", user: "deploy", roles: %w{db}

server "srvz-webapp.he-arc.ch", user: "poweruser", roles: %w{app db web}, port:1447

set :deploy_to, "/var/www/#{fetch(:application)}"

after 'deploy:publishing', 'uwsgi:restart'
after 'deploy:updating', 'python:update_venv'
after 'python:update_venv', 'django:migrate'
after 'django:migrate', 'frontend:compile'

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

    desc 'update venv'
    task :update_venv do
        on roles([:app, :web]) do |h|
            execute "python3 -m venv #{venv_path}"
            execute "source #{venv_path}/bin/activate" 
            execute "#{venv_path}/bin/pip install -r #{release_path}/backend/requirements.txt"
        end
    end
end

namespace :django do

    def venv_path
        File.join(shared_path, 'env')
    end

    desc 'Apply migrations'
    task :migrate do
        on roles(:web) do |h|
            execute "#{venv_path}/bin/python #{release_path}/backend/guideme/manage.py migrate"
	    end
    end
    
end

namespace :frontend do
    desc 'compile frontend'
    task :compile do
        on roles(:web) do |h|
	        execute "cd #{release_path}/frontend"
            execute "npm install"
            execute "npm run build"
	    end
    end
end
