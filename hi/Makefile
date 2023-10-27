# Makefile for assembling and linking hi.asm

# Define the source file and output executable
SOURCE = hi.asm
OUTPUT = hi

# Define the assembler and linker flags
ASFLAGS = -f macho64
LDFLAGS = -macosx_version_min 12.0 -e _main -static

all: $(OUTPUT)

$(OUTPUT): $(SOURCE)
	nasm $(ASFLAGS) -o $(OUTPUT).o $(SOURCE)
	ld $(LDFLAGS) -o $(OUTPUT) $(OUTPUT).o

clean:
	rm -f $(OUTPUT) $(OUTPUT).o

.PHONY: all clean
