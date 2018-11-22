# set -x

# shell中的元素一般是空格分隔的, 如果元素里面有空格, 那么如何才能取出各个元素呢

# 参考:
# Shell 数组
# http://www.runoob.com/linux/linux-shell-array.html
# Bash array with spaces in elements
# https://stackoverflow.com/questions/9084257/bash-array-with-spaces-in-elements

array=("sh run.sh a" # 数组后可以写备注
"sh run.sh b"
)

echo "data is ${array}" # output: data is sh run.sh a, 只能显示第一个元素

echo ${#array[*]}  # array length 2
echo ${#array[@]}  # array length 2


# 使用下标遍历可以满足需求
# output:
# sh run.sh a
# sh run.sh b
for ((i = 0; i < ${#array[@]}; i++)); do
    echo "method1: ${array[$i]}"
done

# 使用"${array[@]}"进行遍历, 能满足需求:
# output:
# sh run.sh a
# sh run.sh b
for ele in "${array[@]}"; do
    echo "method2: ${ele}"
done


# 使用${array[@]}进行遍历, 不能满足需求:
# output:
# sh
# run.sh
# a
# sh
# run.sh
# b
for ele in ${array[@]}; do
    echo "bad method: ${ele}"
done