# Makefile

PROG	= nokia
CC	= cc
CFLAGS	= -O2
LIBS	= -lwiringPi -lpthread

all:
	$(CC) $(CFLAGS) fontx.c pcd8544.c nokia.c $(LIBS) -o $(PROG)

clean:
	-@rm -rf *.o 2>/dev/null || true
	-@rm -rf $(PROG) 2>/dev/null || true
