<template>
 	<view>
		<u-toast ref="uToast" />
 		<u-gap height="40"></u-gap>
 		<view class="deptOne">
 			<text class="title">部门名字</text>
			<u-gap height="10"></u-gap>
 			<u-input type="text" :border="true" placeholder="请输入部门名字" v-model="deptname"/>
 			<u-gap height="30"></u-gap>
 			<text class="title">部门描述</text>
 			<u-gap height="10"></u-gap>
 			<u-input type="textarea" height="400" :border="true" placeholder="请输入部门描述" v-model="remark"/>
 			<u-gap height="30"></u-gap>
			<text class="title">部门照片</text>
			<u-gap height="10"></u-gap>
			<u-input type="textarea" height="300" :border="true" placeholder="请输入部门照片网址" v-model="url"/>
			<u-gap height="50"></u-gap>
 			<u-col span="400">
 				<u-row gutter="20">
					<u-modal v-model="show" :content="content" :show-cancel-button="true" @confirm="confirm" @cancel="cancel"></u-modal>
 					<button @click="submit" type="primary">提交</button>
 				</u-row>
 			</u-col>
 		</view>
 	</view>
 </template>

<script>
</script>
	
<style>
 	.deptOne{
 		margin: 0 50rpx;
 	}
	.title{
		font-size: larger;
		font-weight: bold;
	}
 </style>