#coding:utf-8
#Read subtitles with '.srt' . And change the format of the file and
#leave the subtitle only with the content in a new file
#Date:2015.11.22
#By YE Zhe
import os.path
import chardet
import argparse
import os

# Read all .srt files in 'p' directory and put all of it into list.
def ReadSubFiles(p):
    print p
    result=[]
    list_dirs=os.walk(p)
    srt_files_path=[]
    for root,dirs,files in list_dirs:
        for f in files:
            print f
            if os.path.splitext(f)[1]=='.srt':
                srt_files_path.append(os.path.join(root,f))

    for f in srt_files_path:
        print f
        input_f=open(f)
        code=chardet.detect(input_f.read())
        input_f.close()
        print code
        input_f=open(f)
        line=input_f.readline()
        while line!="":
            try:
                if code['encoding'].find('utf') ==-1 and code['encoding'].find('UTF')==-1:
                    line=line.decode(code['encoding'])
                if line.find('-->')!=-1:
                    line=input_f.readline().strip()
                    if code['encoding'].find('utf') ==-1 and code['encoding'].find('UTF')==-1:
                        line=line.decode(code['encoding'])
                    print line
                    if line!="":
                        result.append(line)
            except BaseException,e:
                print e
                print "There is something wrong with decode."
            line=input_f.readline()
        input_f.close()
        print f
    return result

def ConvertToUTF8(str):
    result=str
    if isinstance(str,unicode)==False:
        try:
            result=str.decode('gb2312')
        except BaseException,e:
            print 'not gb2312'
            result=str.decode('GBK')
        finally:
            try:
                result=result.encode('UTF-8')
            except BaseException,e:
                print e
                return ""
    return result

def newConvertToUTF8(line,code,line_no=0):
    result=line
    try:
        line=line.decode(code['encoding'])
    except BaseException,e:
        print "There is something wrong with decode at line %s" % (str(line_no))
        print e
    finally:
        try:
            result=line.encode('UTF-8')
            return result
        except BaseException,e:
            print "There is something wrong with encode at line %s" % (str(line_no))
            print e
            return ""

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--input",help="the subs need convert")
    parser.add_argument("-o","--output",help="the output file,default is +_utf8",default="")
    parser.add_argument("-r","--replace",action="store_true",help="this flag will cause the file replace,it's convinient but risky")
    args=parser.parse_args()
    if args.replace:
        file_name=args.input
    else:
        if args.output=="":
            file_name="utf8_"+args.input
    tmp_output_file_name='.tmp'+file_name
    output_file=open(tmp_output_file_name,'w')

    # detect code format
    f=open(args.input,'r')
    code=chardet.detect(f.read())
    f.close()

    f=open(args.input,'r')
    line=f.readline()
    line_no=1
    while line!="":
        line=newConvertToUTF8(line,code,line_no=line_no)
        output_file.write(line)
        line=f.readline()
        line_no+=1
    f.close()
    output_file.close()

    os.rename(tmp_output_file_name,file_name)

