#!/bin/sh

until pg_isready -h postgres -p 5432 -d "$POSTGRES_DB" -U "$POSTGRES_USER"; do
    sleep 1
done

exec "$@"
