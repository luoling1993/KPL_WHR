# KPL_WHR



- 比赛数据只抽取了kpl2018秋季赛至2018-11-04号的所有比赛的数据

- __WHR__(Whole History Rating)是基于历史比赛计算当前实力的算法，一般用户围棋世界排名。

- WHR对于时间距今越长的比赛所占权重越小，对于当前强队赢弱队，强队赢的分数较小，弱队输的分数也较小，但是对于当前弱队赢强队，弱队赢的分数较大，强队输的分数也较大，差距越悬殊体现越明显。


### 参考文献

- [wiki](https://en.wikipedia.org/wiki/Go_ranks_and_ratings)
- [paper](https://www.remi-coulom.fr/WHR/WHR.pdf)
- [go rating](https://www.goratings.org/en/)
- [whr github](https://github.com/pfmonville/whole_history_rating)