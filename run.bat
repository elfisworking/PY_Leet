for %%i in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16) do (
    echo %%i test
    robot -d robotoutput 自己补全
    timeout /T 10800
)