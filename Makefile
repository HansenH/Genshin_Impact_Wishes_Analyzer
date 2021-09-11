CC = thrift2pyi

all: idl
idl: common/idl/*.thrift
	$(CC) common/idl/*.thrift
	mv common/idl/const_thrift.pyi common/idl/const_thrift.py