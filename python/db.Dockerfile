FROM postgres:latest

COPY src/resources/db/Jobs.sql /docker-entrypoint-initdb.d/Jobs.sql
COPY src/resources/db/ExtractConfig.sql /docker-entrypoint-initdb.d/ExtractConfig.sql
