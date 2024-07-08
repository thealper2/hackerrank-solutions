declare -A a

draw_triangle() {
    local depth=$1 length=$2 row=$3 col=$4
    [[ $depth -eq 0 ]] && return
    for ((i=length; i>0; i--)); do
        a[$((row-i)).$col]=1
    done
    row=$((row - length))
    for ((i=length; i>0; i--)); do
        a[$((row-i)).$((col-i))]=1
        a[$((row-i)).$((col+i))]=1
    done
    draw_triangle $((depth - 1)) $((length / 2)) $((row - length)) $((col - length))
    draw_triangle $((depth - 1)) $((length / 2)) $((row - length)) $((col + length))
}

read -r n
draw_triangle "$n" 16 63 49

for ((i=0; i<63; i++)); do
    for ((j=0; j<100; j++)); do
        if [[ ${a[$i.$j]} ]]; then
            printf "1"
        else
            printf "_"
        fi
    done
    echo
done
