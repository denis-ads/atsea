from alpine
#from scratch

RUN adduser -D payment
USER payment
COPY process.sh /home/payment/process.sh
CMD /home/payment/process.sh
