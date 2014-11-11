
#### Configure camera driver ##########################

sudo pkill uv4l
sudo uv4l --driver raspicam --auto-video_nr --nopreview



#### IPS-Node update #################################

# git pull origin master

# Removed temporarily. Updates src from github.com/noahingham/IPS-Nodes



#### Start IPS-Node ###################################

cd src
python colourRec.py



