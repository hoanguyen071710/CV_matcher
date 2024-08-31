
CREATE SCHEMA "Config";

CREATE TABLE "Config"."ExtractConfig" (
    id SERIAL PRIMARY KEY,
    site_name TEXT, -- Using TEXT[] to handle the optional List of strings
    search_term TEXT,
    location TEXT,
    distance INTEGER DEFAULT 50 CONSTRAINT check_distance CHECK (distance > 0),
    is_remote BOOLEAN DEFAULT FALSE,
    job_type TEXT,
    easy_apply BOOLEAN,
    results_wanted INTEGER DEFAULT 15 CONSTRAINT check_results_wanted CHECK (results_wanted > 0),
    country_indeed TEXT DEFAULT 'vietnam',
    hyperlinks BOOLEAN DEFAULT FALSE,
    proxies TEXT[], -- Using TEXT[] to handle the optional List of strings
    description_format TEXT DEFAULT 'markdown',
    linkedin_fetch_description BOOLEAN DEFAULT FALSE,
    linkedin_company_ids INTEGER[], -- Using INTEGER[] to handle the optional List of integers
    "offset" INTEGER DEFAULT 0,
    hours_old INTEGER,
    enforce_annual_salary BOOLEAN DEFAULT FALSE,
    "verbose" INTEGER DEFAULT 2,
    kwargs JSONB -- Using JSONB to store the optional dictionary
);


INSERT INTO "Config"."ExtractConfig" (
    site_name,
    search_term,
    location,
    distance,
    is_remote,
    job_type,
    easy_apply,
    results_wanted,
    country_indeed,
    hyperlinks,
    proxies,
    description_format,
    linkedin_fetch_description,
    linkedin_company_ids,
    "offset",
    hours_old,
    enforce_annual_salary,
    "verbose",
    kwargs
) VALUES (
    'example_site_name',
    'example_search_term',
    'example_location',
    50,
    FALSE,
    'example_job_type',
    TRUE,
    15,
    'vietnam',
    FALSE,
    '{"proxy1", "proxy2"}',
    'markdown',
    FALSE,
    '{123, 456}',
    0,
    NULL,
    FALSE,
    2,
    '{"key1": "value1", "key2": "value2"}'
);

