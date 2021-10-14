# Footprint
Record your past

## package
打包你的文件内容，打包项目文件还是用的pyinstall



## example
```bash
# 获取帮助
python main.py --help
# 记录内容
➜  Footprint git:(master) ✗ python main.py input -i CMN-NM-HHH2-S01@上架@测试备注
➜  Footprint git:(master) ✗ python main.py input -i CMN-NM-HHH2-S02@下架@测试备注
➜  Footprint git:(master) ✗ python main.py input -i CMN-NM-HHH2-S02@添加20G上联口@测试备注
➜  Footprint git:(master) ✗ python main.py input -i CMN-NM-HHH2-S02@端口改动@测试备注
➜  Footprint git:(master) ✗ python main.py input -i CMN-NM-HHH2-S03@端口改动@测试备注
➜  Footprint git:(master) ✗ python main.py input -i CMN-NM-HHH2-S03@端口改动@测试备注注
# 展示内容
➜  Footprint git:(master) ✗ python main.py show --all                                
2021-10-14 14:47:50  CMN-NM-HHH2-S03  端口改动  测试备注 
2021-10-14 14:47:48  CMN-NM-HHH2-S03  端口改动  测试备注 
2021-10-14 14:47:46  CMN-NM-HHH2-S02  端口改动  测试备注 
2021-10-14 14:47:40  CMN-NM-HHH2-S02  添加20G上联口  测试备注 
2021-10-14 14:47:25  CMN-NM-HHH2-S02  下架  测试备注 
2021-10-14 14:47:15  CMN-NM-HHH2-S01  上架  测试备注 
# 关键词过滤
➜  Footprint git:(master) ✗ python main.py show -k 下架  
2021-10-14 CMN-NM-HHH2-S02  下架  测试备注
➜  Footprint git:(master) ✗ python main.py show -k 下架 -k 上架
2021-10-14 CMN-NM-HHH2-S02  下架  测试备注 
2021-10-14 CMN-NM-HHH2-S01  上架  测试备注 
# 时间过滤 指定某个月
➜  Footprint git:(master) ✗ python main.py show -m 10 
# 时间过滤 指定几天前
➜  Footprint git:(master) ✗ python main.py show -d 10 
```

## future
- 匹配内容高亮显示
- 多角色内容合并
- 正则匹配
