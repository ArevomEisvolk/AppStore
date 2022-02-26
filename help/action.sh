#sudo apt-get install jq

obj="{"
count=0
for dir in ../Apps/*; do
    count=$(count+=1)
    result=$(cat ./$dir/appfile.json)
    tagline=$(echo "$result" | jq .tagline)
    title=$(echo "$result" | jq .title)
    overview=$(echo "$result" | jq .overview)
    id="$count"
    content="{"id": ${id} , \"tagline\": ${tagline} , \"overview\":${overview} },"
    obj="${obj} ${title} : ${content}"
done
obj=${obj%?}
obj="${obj} }"
data=$(echo "$obj" | jq .)
echo "$data" > ../../config/appfile.json
