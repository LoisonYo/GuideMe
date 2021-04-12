# config valid for current version and patch releases of Capistrano
lock "~> 3.16.0"

set :application, "GuideMe"
set :repo_url, "git@github.com:HE-Arc/GuideMe.git"
set :branch, 'main'

# Default branch is :master
# ask :branch, `git rev-parse --abbrev-ref HEAD`.chomp
