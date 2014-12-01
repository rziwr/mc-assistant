if [ "$HOSTNAME" = "X61s" ]; then
   echo "We are on ${HOSTNAME} so let's push!"
   git push origin master --tags
else
   echo "We are on ${HOSTNAME} and not on X61s"
fi
