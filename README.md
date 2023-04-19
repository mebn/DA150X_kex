# DA150X_kex

## profile
CPU:
```
X=mk01 && make cpu-prof && ./main_cpu.exe ./data/$X.fjs && gprof main_cpu.exe | gprof2dot | dot -Tpdf -o gprof/$X.pdf
```
