DOC=FreeRTOS-on-PIC-18-for-mere-m0rtals

rm -rf pdf
mkdir pdf
cp * pdf
cd pdf
diff -u ../../../PIC_Projects/FreeRTOS/Source/portable/PIC18/18lf45k22_g.lkr ../../../PIC_Projects/FreeRTOS/Source/portable/PIC18/18lf45k22_g_FreeRTOS.lkr > linker-script.diff
git diff 18f2620-original ../../../PIC_Projects/FreeRTOS/Source/portable/PIC18/heap_config.h > heap-config.diff
git diff 18f2620-original ../../../PIC_Projects/FreeRTOS/Source/portable/PIC18/port.c > port-c.diff

pdflatex $DOC
bibtex $DOC
pdflatex $DOC
acroread $DOC.pdf
cd ..

#rm -rf html
#mkdir html
#cd html
#cp ../* .
#htlatex $DOC
#cd ..
