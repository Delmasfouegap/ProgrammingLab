# 1- Prima funzione per stampare il contenuto del file in modo alineato

address_book_view(){
    if [ -f "$1" ]; then
        column -s, -t "$1" | sort -k4
        echo "$1"
    else
        echo "il file $1 non esiste"
    fi
}
#address_book_view "address-book-database.csv"



# ## 2- seconda funzione per ricercare una stringa precisa

address_book_search(){
    IFS=$'\n'
    unico=$(grep -iw "$1" "address-book-database.csv" | tail -n +2)
    if [ -z "$unico" ]; then
        echo "Not found"
        return 1
    fi
    for element in $unico; do
        IFS=',' read -r name surname phone mail city address <<< "$element"
        echo  "name: $name"
        echo  "surname: $surname"
        echo  "phone: $phone"
        echo  "mail: $mail"
        echo  "city: $city"
        echo  "address: $address"
    done
}
#address_book_search "trieste"



##3-funzione per cancelare la riga

address_book_insert(){
    echo "insert the name"
    read name
    echo "insert the surname"
    read surname
    echo "insert the phone"
    read phone
    echo "insert the mail"
    read mail
    if tail -n +2 "$1" | cut -d',' -f4 | grep -Fqi "^$mail"; then
        echo "Errore! questa indirizzo mail esiste già"
        exit 1
    
    else
        echo "insert the city"
        read city
        echo "insert the address"
        read address

       lista_val="$name,$surname,$phone,$mail,$city,$address"

        echo "$lista_val" >> "$1"
        echo "Added" 
        echo " voce ben aggiunta!"
        exit

    fi

}
#address_book_insert "address-book-database.csv"


address_book_delete(){
    echo "insert the mail"
    read mail
    if grep -q "$mail" "$1";then
        grep -ivw $mail "$1" > temp && mv temp "$1"   
        echo "Deleted"
    else
        echo " Cannot find any record"
    fi
}
#address_book_delete "address-book-database.csv"


##per manipolare le diverse funzione a traverso il terminale
case "$1"
    view)  address_book_view "$2" ;;
    search) address_book_search "$2" ;;
    insert) address_book_insert "$2";;
    delete) address_book_delete "$2" ;;
esac