<template>
  <section>
    <!--工具条-->
    <el-col :span="24" class="toolbar">
      <el-form :inline="true" :model="formInline" class="demo-form-inline">
        <el-form-item>
          <el-input v-model="formInline.user" placeholder="主题"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button>查询</el-button>
        </el-form-item>
      </el-form>
    </el-col>

    <!--列表-->
    <template>
      <el-table :data="tableData" highlight-current-row v-loading="listLoading" style="width: 100%;">
        <el-table-column type="index" width="50">
        </el-table-column>
        <el-table-column inline-template label="主题" width="180" sortable>
          <div>
            <router-link to="/tasks/detail" class="name-link">
              <span style="color: #20A0FF;">
                {{ row.name }}
              </span>
            </router-link>
          </div>
        </el-table-column>
        <el-table-column prop="sex" label="类型" width="100" :formatter="formatSex" sortable>
        </el-table-column>
        <el-table-column prop="age" label="状态" width="100" sortable>
        </el-table-column>
        <el-table-column prop="birth" label="优先级" width="180" sortable>
        </el-table-column>
        <el-table-column prop="addr" label="地址" sortable>
        </el-table-column>
        <el-table-column inline-template :context="_self" label="操作" width="100">
          <span>
          <el-button type="text" size="small" @click="handleDel(row)">删除</el-button>
        </span>
        </el-table-column>
      </el-table>
    </template>

    <!--分页-->
    <el-col :span="24" class="toolbar" style="padding-bottom:10px;">
      <el-pagination :current-page="1" :page-sizes="[100, 200, 300, 400]" :page-size="100" layout="total, sizes, prev, pager, next, jumper"
        :total="400" style="float:right">
      </el-pagination>
    </el-col>

    <!--编辑界面-->
    <el-dialog :title="editFormTtile" v-model="editFormVisible" :close-on-click-modal="false">
      <el-form :model="editForm" label-width="80px" :rules="editFormRules" ref="editForm">
        <el-form-item label="姓名" prop="name">
          <el-input v-model="editForm.name" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="性别">
          <!--<el-select v-model="editForm.sex" placeholder="请选择性别">
            <el-option label="男" :value="1"></el-option>
            <el-option label="女" :value="0"></el-option>
          </el-select>-->
          <el-radio-group v-model="editForm.sex">
            <el-radio class="radio" :label="1">男</el-radio>
            <el-radio class="radio" :label="0">女</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="年龄">
          <el-input-number v-model="editForm.age" :min="0" :max="200"></el-input-number>
        </el-form-item>
        <el-form-item label="生日">
          <el-date-picker type="date" placeholder="选择日期" v-model="editForm.birth"></el-date-picker>
        </el-form-item>
        <el-form-item label="地址">
          <el-input type="textarea" v-model="editForm.addr"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click.native="editFormVisible = false">取 消</el-button>
      </div>
    </el-dialog>
  </section>
</template>

<script>
  import NProgress from 'nprogress';

  export default {
    data() {
      return {
        formInline: {
          user: '',
        },
        pickerOptions0: {
          disabledDate(time) {
            return time.getTime() < Date.now() - 8.64e7;
          },
        },
        value1: '',
        editFormVisible: false, // 编辑界面显是否显示
        editFormTtile: '编辑', // 编辑界面标题
        // 编辑界面数据
        editForm: {
          id: 0,
          name: '',
          sex: -1,
          age: 0,
          birth: '',
          addr: '',
        },
        editLoading: false,
        btnEditText: '提 交',
        editFormRules: {
          name: [
            { required: true, message: '请输入姓名', trigger: 'blur' },
          ],
        },
        tableData: [{
          id: 1000,
          name: 'A',
          sex: 1,
          age: '已完成',
          birth: '一般',
          addr: 'A',
        }, {
          id: 1001,
          name: 'B',
          sex: 1,
          age: '已完成',
          birth: '高',
          addr: 'B',
        }],
        listLoading: false,
      };
    },
    methods: {
      // 性别显示转换
      formatSex() {
        // return row.sex === 1 ? '男' : row.sex === 0 ? '女' : '未知';
        return '需求';
      },
      // 删除记录
      handleDel(row) {
        // console.log(row);
        const _ = this;
        this.$confirm('确认删除该记录吗?', '提示', {
          // type: 'warning'
        }).then(() => {
          _.listLoading = true;
          NProgress.start();
          setTimeout(() => {
            for (let i = 0; i < _.tableData.length; i += 1) {
              if (_.tableData[i].id === row.id) {
                _.tableData.splice(i, 1);

                _.listLoading = false;
                NProgress.done();
                _.$notify({
                  title: '成功',
                  message: '删除成功',
                  type: 'success',
                });
                break;
              }
            }
          }, 1000);
        }).catch(() => {
        });
      },
      // 显示新增界面
      handleAdd() {
        this.editFormVisible = true;
        this.editFormTtile = '新增';
        this.editForm.id = 0;
        this.editForm.name = '';
        this.editForm.sex = 1;
        this.editForm.age = 0;
        this.editForm.birth = '';
        this.editForm.addr = '';
      },
    },
  };
</script>

<style scoped>
  .toolbar .el-form-item {
    margin-bottom: 10px;
  }
  
  .toolbar {
    background: #fff;
    padding: 10px 10px 0px 10px;
  }
  .name-link {
    text-decoration: none;
  }
</style>
