exchange setting :
exchange "jalur_khusus", Type : fanout, Durability : Transient
Untuk "with_queue_generator" harus menggunakan type exchange "fanout", data yg diterima akan hilang tanpa ditanpung oleh QUEUE

exchange setting :
exchange "jalur_khusus", Type : direct, Durability : Durable
exchange "jalur_lambat", Type : direct, Durability : Durable
untuk "antrian.py" dan "receive.py" data yg masuk melalui exchange di pilah dan dimasukkan kedalam QUEUE