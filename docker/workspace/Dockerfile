# Set the base image to Ubuntu
FROM        ubuntu
MAINTAINER TaoBeier <zhangjintao9020@gmail.com>

RUN echo "deb http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse\ndeb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse\ndeb http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse\ndeb-src http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse\ndeb-src http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse\ndeb-src http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse\n" > /etc/apt/sources.list

RUN apt-get -qqy update
RUN apt-get install -qqy python vim git wget
RUN cd /home && wget https://raw.githubusercontent.com/tao12345666333/vim/master/vimrc -O $HOME/.vimrc && vim -E -u $HOME/.vimrc +qall
