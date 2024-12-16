# -*- coding:utf-8 -*-

import sys
import gzip

def run(dirs_path):
    with open(dirs_path, 'rb') as f:
        name = dirs_path.split('/')[-1].split('.')[0]
        w = open('/GPUFS/sysu_dcli_1/Bismark/convert/' + name + '.txt', 'w')
        w.write('chr'+'\t'+'pos'+'\t'+'N'+'\t'+'X'+'\n')
        
        if dirs_path.endswith('.gz'):
            with gzip.open(f, 'rt') as gz_f:
                for line in gz_f:
                    d = line.strip().split('\t')
                    col_3 = int(d[-2]) + int(d[-1])
                    w.write(d[0] + '\t' + d[1] + '\t' + str(col_3) + '\t' + d[-1] + '\n')
        else:
            for line in f:
                d = line.strip().split('\t')
                col_3 = int(d[-2]) + int(d[-1])
                w.write(d[0] + '\t' + d[1] + '\t' + str(col_3) + '\t' + d[-1] + '\n')
        
        w.close()

if __name__ == '__main__':
    dirs_path = sys.argv[1]
    run(dirs_path)
