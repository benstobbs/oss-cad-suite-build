cd riscv-gnu-toolchain
./configure --prefix=${INSTALL_PREFIX}
make DESTDIR=${OUTPUT_DIR} -j${NPROC}