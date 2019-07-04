# 函数, 要点: $#, local
function copy_data(){
    if [ $# != 2 ]; then
        return 1
    fi
    local from="${1}"
    local to="${2}"
    cp -r ${from} ${to}
}
