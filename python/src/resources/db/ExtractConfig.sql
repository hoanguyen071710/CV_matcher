
CREATE SCHEMA Config;

CREATE TABLE ExtractConfig (
    id SERIAL PRIMARY KEY,
    site_name TEXT, -- Using TEXT[] to handle the optional List of strings
    search_term TEXT,
    location TEXT,
    distance INTEGER DEFAULT 50,
    is_remote BOOLEAN DEFAULT FALSE,
    job_type TEXT,
    easy_apply BOOLEAN,
    results_wanted INTEGER DEFAULT 15,
    country_indeed TEXT DEFAULT 'vietnam',
    hyperlinks BOOLEAN DEFAULT FALSE,
    proxies TEXT[], -- Using TEXT[] to handle the optional List of strings
    description_format TEXT DEFAULT 'markdown',
    linkedin_fetch_description BOOLEAN DEFAULT FALSE,
    linkedin_company_ids INTEGER[], -- Using INTEGER[] to handle the optional List of integers
    offset INTEGER DEFAULT 0,
    hours_old INTEGER,
    enforce_annual_salary BOOLEAN DEFAULT FALSE,
    verbose INTEGER DEFAULT 2,
    kwargs JSONB -- Using JSONB to store the optional dictionary
);
