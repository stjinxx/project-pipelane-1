with source as (
        SELECT * FROM {{source('olist', 'olist_customers')}}
),

renamed as (
    SELECT 
        customer_id,
        customer_unique_id,
        customer_zip_code_prefix::int as zip_code_prefix,
        customer_city                 as city,
        customer_state                as state
    FROM source
)
SELECT * FROM renamed