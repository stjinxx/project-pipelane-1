with source as (
    SELECT * FROM {{source('olist', 'olist_order_items')}}
),

renamed as (
    SELECT 
        order_id,
        order_item_id::int                      as order_item_id,
        product_id,
        seller_id,
        cast(shipping_limit_date as timestamp)     as shipping_limit_at,
        price::numeric(10,2)                    as price,
        freight_value::numeric(10,2)            as freight_value
    FROM source
)
SELECT * FROM renamed