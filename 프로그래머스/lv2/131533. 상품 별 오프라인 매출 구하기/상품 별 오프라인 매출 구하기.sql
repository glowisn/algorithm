-- 코드를 입력하세요
WITH sales_amount AS (
SELECT product_id , SUM(sales_amount) as sale
FROM OFFLINE_SALE
GROUP BY product_id)
SELECT P.product_code, (sa.sale * P.price) as SALES
FROM PRODUCT P, sales_amount sa
WHERE p.product_id = sa.product_id
ORDER BY SALES DESC, P.product_code ASC
