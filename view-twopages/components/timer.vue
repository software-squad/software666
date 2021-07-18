 <template>
        <view class="content">
            <view class="data">
                <text>{{val}}</text>
            </view>
            <button type="primary" @click="comunicationOff">结束监听</button>
        </view>
    </template>

    <script>
        export default {
			name:'timer',
            data() {
                return {
                    val: 0
                }
            },
            onLoad() {
                setInterval(()=>{
                    uni.$emit('add', {
                        data: 2
                    })
                },1000)
                uni.$on('add', this.add)
            },
            methods: {
                comunicationOff() {
                    uni.$off('add', this.add)
                },
                add(e) {
                    this.val += e.data
                }
            }
        }
    </script>

    <style>
        .content {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .data {
            text-align: center;
            line-height: 40px;
            margin-top: 40px;
        }

        button {
            width: 200px;
            margin: 20px 0;
        }
    </style>