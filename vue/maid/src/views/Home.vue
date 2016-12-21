<template>
  <el-row class="panel">
    <el-col :span="24" class="panel-top">
      <el-col :span="8" style="font-size:26px;">
        <!--<img src="../assets/logo4.png" class="logo">-->
        <i class="fa fa-paper-plane"></i>
        <span>Maid<i style="color:#20a0ff">Platform</i></span>
      </el-col>
      <el-col :span="12">
        <el-menu theme="dark" mode="horizontal">
          <router-link to="/tasks/all">
            <el-menu-item index="1">
              所有
            </el-menu-item>
          </router-link>
          <el-submenu index="2">
            <template slot="title">我的</template>
            <router-link to="/tasks/ready">
              <el-menu-item index="2-1">未开始</el-menu-item>
            </router-link>
            <router-link to="/tasks/running">
              <el-menu-item index="2-2">进行中</el-menu-item>
            </router-link>
            <router-link to="/tasks/finish">
              <el-menu-item index="2-3">已完成</el-menu-item>
            </router-link>
          </el-submenu>
        </el-menu>
      </el-col>
      <el-col :span="4">
        <el-tooltip class="item tip-logout" effect="dark" content="退出" placement="bottom" style="padding:0px;">
          <i class="fa fa-sign-out" aria-hidden="true" v-on:click="logout"></i>
        </el-tooltip>
      </el-col>
    </el-col>
    <el-col :span="24" class="panel-center">
      <aside style="width:230px;">
        <h5 class="admin">
          <i class="fa fa-user" aria-hidden="true" style="margin-right:5px;">
          </i>
          喵喵~
        </h5>
        <el-menu style="border-top: 1px solid #475669;" default-active="/online" class="el-menu-vertical-demo" @open="handleopen"
          @close="handleclose" @select="handleselect" theme="dark" unique-opened router>
          <template v-for="(item,index) in $router.options.routes" v-if="!item.hidden">
            <el-submenu :index="index+''" v-if="!item.leaf">
              <template slot="title"><i :class="item.iconCls"></i>{{item.name}}</template>
              <el-menu-item v-for="child in item.children" :index="child.path">{{child.name}}</el-menu-item>
            </el-submenu>
            <el-menu-item v-if="item.leaf&&item.children.length>0" :index="item.children[0].path"><i :class="item.iconCls"></i>{{item.children[0].name}}</el-menu-item>
          </template>
        </el-menu>
      </aside>
      <section class="panel-c-c">
        <div class="grid-content bg-purple-light">
          <el-col :span="24" style="margin-bottom:15px;">
            <strong style="width:200px;float:left;color: #475669;">{{currentPathName}}</strong>
          </el-col>
          <el-col :span="24" style="background-color:#fff;box-sizing: border-box;">
            <transition name="fade">
              <router-view></router-view>
            </transition>
          </el-col>
        </div>
      </section>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    data() {
      return {
        currentPathName: '这里是名字',
        currentPathNameParent: '导航一',
        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: '',
        },
      };
    },
    // watch: {
    //   '$route' (to, from) { // 监听路由改变
    //     this.currentPathName=to.name;
    //     this.currentPathNameParent=to.matched[0].name;
    //   }
    // },
    methods: {
      onSubmit() {
        // console.log('submit!');
      },
      handleopen() {
        // console.log('handleopen');
      },
      handleclose() {
        // console.log('handleclose');
      },
      handleselect() {
      },
      // 退出登录
      logout() {
        const _ = this;
        this.$confirm('确认退出吗?', '提示', {
          // type: 'warning'
        }).then(() => {
          _.$router.replace('/login');
        }).catch(() => {
        });
      },
    },
  };
</script>

<style scoped>
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity .5s
  }
  
  .fade-enter,
  .fade-leave-active {
    opacity: 0
  }
  
  .panel {
    position: absolute;
    top: 0px;
    bottom: 0px;
    width: 100%;
  }
  
  .panel-top {
    height: 60px;
    line-height: 60px;
    background: #1F2D3D;
    color: #c0ccda;
  }
  
  .panel-center {
    background: #324057;
    position: absolute;
    top: 60px;
    bottom: 0px;
    overflow: hidden;
  }
  
  .panel-c-c {
    background: #f1f2f7;
    position: absolute;
    right: 0px;
    top: 0px;
    bottom: 0px;
    left: 230px;
    overflow-y: scroll;
    padding: 20px;
  }
  
  .logout {
    background-size: contain;
    width: 20px;
    height: 20px;
    float: left;
  }
  
  .logo {
    width: 40px;
    float: left;
    margin: 10px 10px 10px 18px;
  }
  
  .tip-logout {
    float: right;
    margin-right: 20px;
    padding-top: 5px;
  }
  
  .tip-logout i {
    cursor: pointer;
  }
  
  .admin {
    color: #c0ccda;
    text-align: center;
  }
</style>
