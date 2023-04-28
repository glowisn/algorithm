-- 코드를 입력하세요
SELECT P.product_code, sum(price * sales_amount) as sales
from PRODUCT as P, OFFLINE_SALE as OS
where OS.product_id = P.product_id
group by P.product_code
having sum(price * sales_amount)
order by 2 desc, 1 asc;