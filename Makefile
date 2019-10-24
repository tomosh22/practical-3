include ../make-inc/Makefile.inc
-include makefile-local

all: csc1034-project-3_web.html readme

csc1034-project-3_web.html: csc1034-project-3.md

readme:
	cp csc1034-project-3.md README.md

publish:
	- mkdir $(PUBLISH)/project-3
	cp csc1034-project-3_web.html $(PUBLISH)/project-3
	cp -r ./img $(PUBLISH)/project-3/img

clean:
	rm csc1034-project-3_web.html
