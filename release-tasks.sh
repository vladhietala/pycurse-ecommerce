# release-tasks.sh

## Step to execute
python3 manage.py migrate

# check for a good exit
if [ $? -ne 0 ]
then
  # something went wrong; convey that and exit
  exit 1
fi

# other code, potentially
