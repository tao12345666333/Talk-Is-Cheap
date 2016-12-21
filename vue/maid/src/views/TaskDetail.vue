<template>
  <el-col :span="24" style="width: 100%;">
    <el-row>
      <el-col :span="12">
        <el-form ref="form" label-width="80px" style="margin:20px;">
          <el-form-item label="名称">
            API
          </el-form-item>
        </el-form>
      </el-col>
      <el-col :span="12">
        <div>
          <h3>状态</h3>
          <div style="margin-left:20%;">
            <el-progress type="circle" :percentage="80"></el-progress>
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row style="border-top: dashed 1px #99A9BF;">
      <h2>变更记录</h2>
      <el-col :span="24">
        <el-row style="margin-top: 20px; padding: 20px; border-top: dashed 1px #99A9BF;">
          <el-steps :space="200" :active="1" style="margin-top: 20px;">
            <el-step title="verify" description="验证"></el-step>
            <el-step title="build" description="编译"></el-step>
            <el-step title="push" description="push"></el-step>
          </el-steps>
        </el-row>
        <el-row>
        </el-row>
      </el-col>
    </el-row>
  </el-col>
</template>
<script>
  export default {
  };
</script>
