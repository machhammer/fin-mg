cd /Users/machhammer/Documents/projects/fin-mg


echo '****** FRONTEND'

ng build --prod

ssh pi@machhammer.internet-box.ch <<'ENDSSH'
    cd /var/www/html
    sudo rm -r *
    cd /home/pi/fin-mg/fin-mg-server
ENDSSH


cd /Users/machhammer/Documents/projects/fin-mg/dist/fin-mg
scp -r * pi@machhammer.internet-box.ch:/home/pi/fin-mg/fin-mg-server


ssh pi@machhammer.internet-box.ch <<'ENDSSH'
    cd /home/pi/fin-mg/fin-mg-server
    sudo mv * /var/www/html
ENDSSH

echo '****** FRONTEND completed'


echo '****** BACKEND SERVER'

ssh pi@machhammer.internet-box.ch <<'ENDSSH'
    cd /home/pi/fin-mg
    rm -r fin-mg-backend
    mkdir fin-mg-backend
ENDSSH

cd /Users/machhammer/Documents/projects/fin-mg
scp -r fin-mg-backend pi@machhammer.internet-box.ch:/home/pi/fin-mg

ssh pi@machhammer.internet-box.ch <<'ENDSSH'
    cd /home/pi/fin-mg/fin-mg-backend
    python3 -m venv fin-mg-backend-venv
    source fin-mg-backend-venv/bin/activate
    pip install -r requirements.txt
    chmod +x backend/server.py
    chmod +x start_server.sh
    sh start_server.sh
ENDSSH

echo '****** BACKEND SERVER completed.'


