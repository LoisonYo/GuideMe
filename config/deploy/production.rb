# server-based syntax
# ======================
# Defines a single server with a list of roles and multiple properties.
# You can define all roles on a single server, or split them:

# server "example.com", user: "deploy", roles: %w{app db web}, my_property: :my_value
# server "example.com", user: "deploy", roles: %w{app web}, other_property: :other_value
# server "db.example.com", user: "deploy", roles: %w{db}

server "srvz-webapp.he-arc.ch", user: "poweruser", roles: %w{app db web}, port:1447

set :deploy_to, "/var/www/#{fetch(:application)}"


after 'deploy:publishing', 'django:migrate'

namespace :django do

    def venv_path
        File.join(shared_path, 'env')
    end

    desc 'Apply migrations'
    task :migrate do
        on roles(:web) do |h|
            execute "cp #{shared_path}/.env #{release_path}/backend/guideme/.env"
            execute "source #{venv_path}/bin/activate && python3 #{release_path}/backend/guideme/manage.py migrate && cd #{release_path}/backend &&python3 #{release_path}/backend/guideme/manage.py collectstatic --noinput"
	    end
    end
    
end

after 'django:migrate', 'uwsgi:restart'

namespace :uwsgi do
    desc 'Restart application'
    task :restart do
        on roles(:web) do |h|
	        execute :sudo, 'sv reload uwsgi'
	    end
    end
end

after 'deploy:updating', 'python:update_venv'

namespace :python do

    def venv_path
        File.join(shared_path, 'env')
    end

    desc 'update venv'
    task :update_venv do
        on roles([:app, :web]) do |h|
            execute "source #{venv_path}/bin/activate && #{venv_path}/bin/pip install -r #{release_path}/backend/requirements.txt"
        end
    end
end

after 'deploy:publishing', 'frontend:compile'

namespace :frontend do
    desc 'compile frontend'
    task :compile do
        on roles(:web) do |h|
	        execute "cd #{release_path}/frontend && npm install && npm run build"
	    end
    end
end
