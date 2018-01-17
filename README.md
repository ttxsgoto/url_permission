### Django 基于URL权限管理模块

#### 说明
1. 基于djangorestframework+django-rest-swagger实现
2. 通过URL检查来判断用户是否有权限访问接口
3. 用户和组都可以拥有相应的权限,用户拥有的权限为用户所在组和用户单独拥有权限的并集
4. 通过定义的middleware中间件来检查用户是否拥有相应权限

#### 接口说明
   
- GET /permission/url/    获取URL列表
- GET /permission/group/ 获取权限组对应的权限列表
- POST /permission/group/ 创建组和对应的权限
- PUT /permission/group/{id}/ 更新权限组对应的权限
- GET /permission/user_permission/    获取用户对应的所有权限
- PUT /permission/user_permission/{user} 用户添加组权限/单个权限

#### 使用说明
详见README.rst

