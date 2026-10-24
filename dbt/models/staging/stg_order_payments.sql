with source as (
    select * from {{source('olist','olist_order_payments')}}
),

renamed as (
    select
        order_id,
        payment_sequential::int         as paymentsequential,
        payment_type                    as payment_type,
        payment_installments::int       as installments,
        payment_value::numeric(10, 2)   as payment_value
        from source
)
select * from renamed