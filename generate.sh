#!/usr/bin/bash
# run with bash ./generate.sh
NOOFUSERS=100
ENDPOINTS=4
NOOFBTYPE=3
MAXNOOFGRENADES=100

GENERATEREQS=1000

REQS=0
until [ $REQS -gt $GENERATEREQS ]; do
    ID=$(( ( RANDOM % $NOOFUSERS )  + 1 ))
    EP=$(( ( RANDOM % $ENDPOINTS )  + 1 ))
    BTYPE=$(( ( RANDOM % $NOOFBTYPE )  + 1 ))
    NOOFGRENADES=$(( ( RANDOM % $MAXNOOFGRENADES )  + 1 ))
#    echo $ID $EP
    case $EP in
	1)
#	    echo "grenades"
	    docker-compose exec mids curl -X POST "http://localhost:5000/purchase_grenades?n="$NOOFGRENADES
	    ;;
	2)
#   	    echo "bomb"
	    case $BTYPE in
		1)
		    docker-compose exec mids curl "http://localhost:5000/purchase_bomb/nuclear"
		    ;;
		2)
		    docker-compose exec mids curl "http://localhost:5000/purchase_bomb/armour"
		    ;;
		3)
		    docker-compose exec mids curl "http://localhost:5000/purchase_bomb/blastr"
		    ;;
	    esac
	    ;;
	3)
	    docker-compose exec mids curl -X POST "http://localhost:5000/login?id="$ID
	    ;;
	4)
	    docker-compose exec mids curl -X POST "http://localhost:5000/logout?id="$ID
	    ;;

    esac
    let REQS=REQS+1
done
