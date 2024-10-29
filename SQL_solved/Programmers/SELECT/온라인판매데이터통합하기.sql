with sales as (
    SELECT date_format(sales_date, '%Y-%m-%d'), product_id, user_id, sales_amount
    from online_sale
    where date_format(sales_date, '%Y-%m') = '2022-03'
    UNION ALL
    SELECT date_format(sales_date, '%Y-%m-%d'), product_id, NULL as user_id, sales_amount
    from offline_sale
    where date_format(sales_date, '%Y-%m') = '2022-03'
)

select *
from sales
order by 1, 2, 3