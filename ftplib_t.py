from ftplib import FTP

if __name__ == "__main__":
    r = FTP("192.168.2.206")
    r.login("ftpuser", "ftpuser")
    w = FTP("192.168.2.209")
    w.login("ftpuser", "ftpuser")


JobDatasourceInfo(id=2, jobGroup=1, jobType=1, jobCron=null, jobDesc=dd, addrDescribe=192.168.2.206=>192.168.2.209, typeDescribe=postgresql=>postgresql, projectId=1, addTime=Thu Mar 07 20:40:54 CST 2024, updateTime=Fri Mar 08 02:17:04 CST 2024, userId=1, triggerStatus=1, executeStatus=200, executeType=0, primaryKey=id, writePrimaryKey=id, readerTable=public.t1, readerDatasourceId=1, readerColumns="id","name","age", writeTable=public.t2, writeDatasourceId=2, writeColumns="id","info1","info2", syncMode=2, responsible=文件链路责任人, descInfo=文件业务意图, projectName=null, userName=null, rate=0, rateTime=3200, actuator=master, triggerTable=TOPWALK_DXP_1_TB, randomKey=vOF1T4B4_1, delStatus=0, readerId=3, writeId=0, syncType=1, isDeleteData=0, readerDatasource=JobDatasource(id=null, datasourceName=数据库资源206, datasource=postgresql, datasourceGroup=null, jdbcUsername=UyqCvF9DfPw/640gAaoPRw==, jdbcPassword=UyqCvF9DfPw/640gAaoPRw==, jdbcUrl=jdbc:postgresql://192.168.2.206:5432/test, jdbcDriverClass=org.postgresql.Driver, status=null, createBy=null, createDate=null, updateBy=null, updateDate=null, comments=null, zkAdress=null, databaseName=test, dataIp=192.168.2.206, dataPort=5432, tu=T, jdbcVersion=null, schemaName=null), writeDatasource=JobDatasource(id=null, datasourceName=数据库资源209, datasource=postgresql, datasourceGroup=null, jdbcUsername=UyqCvF9DfPw/640gAaoPRw==, jdbcPassword=UyqCvF9DfPw/640gAaoPRw==, jdbcUrl=jdbc:postgresql://192.168.2.209:5432/test, jdbcDriverClass=org.postgresql.Driver, status=null, createBy=null, createDate=null, updateBy=null, updateDate=null, comments=null, zkAdress=null, databaseName=test, dataIp=192.168.2.209, dataPort=5432, tu=null, jdbcVersion=null, schemaName=null), key=2, keywordsId=null, signatureVerification=2)