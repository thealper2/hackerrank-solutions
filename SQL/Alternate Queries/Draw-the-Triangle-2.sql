SET @I:=0;
SELECT REPEAT("* ", @I:=@I+1) FROM INFORMATION_SCHEMA.TABLES
WHERE @I < 20;