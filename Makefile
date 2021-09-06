CC = thrift2pyi

all: idl
idl: common/idl/*.thrift
	$(CC) common/idl/*.thrift