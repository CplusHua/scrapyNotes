use stock;

DROP TABLE IF EXISTS `SecondNewStock`;
CREATE TABLE `SecondNewStock` (
  `ID`    int(32) unsigned NOT NULL AUTO_INCREMENT,
  `NAME`  varchar(32)    NOT NULL DEFAULT ' ',
  `FXJ`   varchar(32)    NOT NULL DEFAULT ' ',
  `ZTS`   varchar(32)    NOT NULL DEFAULT ' ',
  `QGSY`  varchar(32)    NOT NULL DEFAULT ' ',
  `QGCB`  varchar(32)   NOT NULL DEFAULT ' ',
  `ZJSYL` varchar(32)   NOT NULL DEFAULT ' ',
  `FXL`   varchar(32)   NOT NULL DEFAULT '  ',
  `FXSY`  varchar(32)   NOT NULL DEFAULT '  ',
  `ZQL`   varchar(32)   NOT NULL DEFAULT ' ',
  `SSR`   varchar(32)   NOT NULL DEFAULT ' ',
  `PBR`   varchar(32)   NOT NULL DEFAULT ' ',
  `PBZJ`  varchar(32)   NOT NULL DEFAULT ' ',
  `PBZF`  varchar(32)   NOT NULL DEFAULT ' ',
  `ZXJ`   varchar(32)   NOT NULL DEFAULT ' ',
  `CODE`  varchar(8)    NOT NULL DEFAULT ' ',
  `URL`   varchar(128)   NOT NULL DEFAULT ' ',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `CODE` (`CODE`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8  
comment='新股名称 ,发行价 ,涨停数 ,千股收益 ,千股成本 ,资金收益率 ,发行量 ,发行市盈 ,中签率 ,上市日 ,破板日 ,破板中价 ,破板涨幅 ,最新价';
ALTER TABLE `secondnewstock`
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_bin;
 
insert into SecondNewStock(`NAME`,`FXJ`,`ZTS`,`QGSY`,`QGCB`,`ZJSYL`,`FXL`,`FXSY`,`ZQL`,`SSR`,`PBR`,`PBZJ`,`PBZF`,`ZXJ`,`CODE`,`URL`)
values('新股名称' ,'发行价' ,'涨停数' ,'千股收益' ,'千股成本' ,'资金收益率' ,'发行量' ,'发行市盈' ,
        '中签率'  ,'上市日' ,'破板日' ,'破板中价' ,'破板涨幅' ,'最新价',      '000000','xxx');  

insert into SecondNewStock(`NAME`,`FXJ`,`ZTS`,`QGSY`,`QGCB`,`ZJSYL`,`FXL`,`FXSY`,`ZQL`,`SSR`,`PBR`,`PBZJ`,`PBZF`,`ZXJ`,`CODE`,`URL`)
values('田中精机' ,'7.92' ,'4' ,'7250元(浮盈)' ,'641万' ,'0.11%(浮盈)' ,'3268万' ,'22.98倍' ,
        '0.124%'  ,'20150519' ,'--' ,'--' ,'--' ,'15.17',      '600461','http://quote.cfi.cn/quote_300461.html '); 
 

;
