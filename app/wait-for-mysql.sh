#!/bin/bash
set -e

host="$1"
shift
cmd="$@"

until mysql -h "$host" -u root -proot -e 'SELECT 1'; do
  echo "⏳ En attente de MySQL..."
  sleep 2
done

echo "✅ MySQL est prêt, démarrage de l'application Flask..."
exec $cmd

