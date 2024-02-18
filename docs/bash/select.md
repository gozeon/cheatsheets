## 选择示例

```bash title="select.bash"
#!/bin/bash
PS3="Select item please:"

items=("Item 1" "Item 2" "Item 3")

select item in "${items[@]}" Quit
do
	case $REPLY in
		1)
			echo "#$REPLY $item"
			;;
		2)
			echo "#$REPLY $item"
			;;
		3)	
			echo "#$REPLY $item"
			;;
		
		$((${#items[@]}+1)))
			echo "We're done!";
			break
			;;
		*)
			echo "$((${#items[@]}+1))"
			echo "Ooops - unknown choice $REPLY"
			;;
	esac
done

```
