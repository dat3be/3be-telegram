# Strings / localization file for 3be-telegram in Vietnamese
# Đừng xóa các trường {curly braces} vì chúng được sử dụng trong mã.

# Biểu tượng tiền tệ
currency_symbol = "₫"

# Định dạng vị trí biểu tượng tiền tệ
currency_format_string = "{value} {symbol}"

# Số lượng sản phẩm còn trong kho
in_stock_format_string = "{quantity} còn lại"

# Số lượng sản phẩm trong giỏ hàng
in_cart_format_string = "{quantity} trong giỏ hàng"

# Thông tin sản phẩm
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Số đơn hàng, hiển thị trong thông tin đơn hàng
order_number = "Đơn hàng #{id}"

# Thông tin đơn hàng, hiển thị cho quản trị viên
order_format_string = "bởi {user}\n" \
                      "Tạo vào {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "TỔNG: <b>{value}</b>\n" \
                      "\n" \
                      "Ghi chú khách hàng: {notes}\n"

# Thông tin đơn hàng, hiển thị cho người dùng
user_order_format_string = "{status_emoji} <b>Đơn hàng {status_text}</b>\n" \
                           "{items}\n" \
                           "TỔNG: <b>{value}</b>\n" \
                           "\n" \
                           "Ghi chú: {notes}\n"

# Trang giao dịch đang tải
loading_transactions = "<i>Đang tải giao dịch...\n" \
                       "Vui lòng đợi một chút.</i>"

# Trang giao dịch
transactions_page = "Trang <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# Tiêu đề của file transactions.csv
csv_caption = "📄 File .csv chứa tất cả giao dịch đã lưu trong cơ sở dữ liệu bot.\n" \
              "Bạn có thể mở file này bằng các chương trình như LibreOffice Calc để xử lý dữ liệu."

# Chào mừng sau khi gửi lệnh /start
conversation_after_start = "Xin chào!\n" \
                           "Chào mừng bạn đến với 3be-telegram!\n" \
                           "Đây là phiên bản 🅱️ <b>Beta</b> của phần mềm.\n" \
                           "Phần mềm đã sử dụng được nhưng vẫn có thể gặp lỗi.\n" \
                           "Nếu bạn tìm thấy lỗi, vui lòng báo cáo tại https://github.com/Steffo99/greed/issues."

# Mở menu người dùng
conversation_open_user_menu = "Bạn muốn làm gì?\n" \
                              "💰 Bạn có <b>{credit}</b> trong ví của mình.\n" \
                              "\n" \
                              "<i>Nhấn nút ở bàn phím phía dưới để chọn thao tác.\n" \
                              "Nếu bàn phím không mở, nhấn biểu tượng bốn ô vuông ở thanh tin nhắn.</i>"

# Mở menu quản trị viên
conversation_open_admin_menu = "Bạn là 💼 <b>Quản lý</b> của cửa hàng!\n" \
                               "Bạn muốn làm gì?\n" \
                               "\n" \
                               "<i>Nhấn nút ở bàn phím phía dưới để chọn thao tác.\n" \
                               "Nếu bàn phím không mở, nhấn biểu tượng bốn ô vuông ở thanh tin nhắn.</i>"

# Chọn phương thức thanh toán
conversation_payment_method = "Bạn muốn thêm tiền vào ví của mình bằng cách nào?"

# Xác nhận giỏ hàng
conversation_confirm_cart = "🛒 Giỏ hàng của bạn chứa các sản phẩm sau:\n" \
                            "{product_list}" \
                            "Tổng: <b>{total_cost}</b>\n" \
                            "\n" \
                            "<i>Nhấn nút Xong để tiếp tục hoặc Hủy để quay lại.</i>"

# Hỏi ghi chú cho đơn hàng
ask_order_notes = "Bạn có muốn để lại ghi chú cho đơn hàng này không?\n" \
                  "💼 Quản lý sẽ thấy nội dung này.\n" \
                  "\n" \
                  "<i>Nhập ghi chú hoặc nhấn Bỏ qua nếu không muốn.</i>"

# Hỏi thông tin sản phẩm
ask_product_name = "Tên sản phẩm là gì?"
ask_product_description = "Mô tả sản phẩm là gì?"
ask_product_price = "Giá sản phẩm là bao nhiêu?\n" \
                    "Nhập <code>X</code> nếu bạn chưa muốn sản phẩm được bán ngay."
ask_product_image = "🖼 Hình ảnh nào bạn muốn sử dụng cho sản phẩm này?\n" \
                    "<i>Gửi ảnh hoặc nhấn Bỏ qua nếu không muốn thêm hình ảnh.</i>"

# Giá trị hiện tại khi chỉnh sửa
edit_current_value = "Giá trị hiện tại là:\n" \
                     "<pre>{value}</pre>\n" \
                     "<i>Nhấn nút Bỏ qua bên dưới để giữ nguyên giá trị.</i>"

# Các menu
menu_products = "📝️ Sản phẩm"
menu_orders = "📦 Đơn hàng"
menu_stop = "🛑 Dừng"
menu_order = "🛒 Đặt hàng"
menu_order_status = "🛍 Đơn hàng của tôi"
menu_add_credit = "💵 Nạp tiền"
menu_bot_info = "ℹ️ Thông tin bot"
menu_language = "🌐 Ngôn ngữ"
menu_help = "❓ Trợ giúp / Hỗ trợ"
menu_transactions = "💳 DS giao dịch"
menu_add_product = "✨ Thêm sản phẩm"
menu_delete_product = "❌ Xóa sản phẩm"
menu_add_to_cart = "➕ Thêm vào giỏ"
menu_remove_from_cart = "➖ Bỏ khỏi giỏ"
menu_cancel = "🔙 Hủy"
menu_complete = "✅ Hoàn thành"
menu_refund = "✴️ Hoàn tiền"
menu_skip = "⏭ Bỏ qua"
menu_done = "✅️ Xong"
menu_pay = "💳 Thanh toán"
menu_cash = "💵 Tiền mặt"
menu_credit_card = "💳 Thẻ tín dụng"
menu_vietqr = "💳 VietQR"
menu_edit_credit = "💰 Sửa số dư"
menu_user_mode = "👤 Chuyển sang chế độ khách hàng"
menu_csv = "📄 Xuất file .csv"
menu_edit_admins = "🏵 Sửa Admin"
menu_contact_shopkeeper = "👨‍💼 Liên hệ cửa hàng"
menu_next = "▶️ Sau"
menu_previous = "◀️ Trước"

# Liên hệ quản lý cửa hàng
contact_shopkeeper = "Hiện tại, đội ngũ hỗ trợ khách hàng bao gồm:\n" \
                     "{shopkeepers}\n" \
                     "<i>Nhấn vào tên của họ để bắt đầu trò chuyện trên Telegram.</i>"

# Chọn ngôn ngữ
conversation_language_select = "Chọn một ngôn ngữ:"

# Prompts and messages for VietQR payments
payment_vietqr_amount = "Chọn một số tiền cho thanh toán VietQR:"
vietqr_payment_pending = "Đang chờ xác nhận thanh toán VietQR (Mã giao dịch: {transaction_id}). Vui lòng đợi..."
vietqr_payment_caption = "Quét mã QR để thanh toán ({value_vnd} VND)."
vietqr_payment_timeout_warning = "Hoàn tất thanh toán cho giao dịch {transaction_id} trong vòng 10 phút để tránh bị hủy."
vietqr_payment_timeout = "Phiên thanh toán cho giao dịch {transaction_id} đã hết hạn. Vui lòng bắt đầu giao dịch mới."
vietqr_payment_success = "✅ Thanh toán thành công! Số dư trong ví đã được cập nhật."
vietqr_payment_failed = "❌ Thanh toán VietQR với mã giao dịch: {transaction_id} thất bại. Vui lòng thử lại."

# Error messages
error_vietqr_config = "Cấu hình VietQR bị thiếu hoặc không chính xác. Vui lòng liên hệ bộ phận hỗ trợ."
error_invalid_amount = "Số tiền nhập vào không hợp lệ. Vui lòng thử lại."
error_invalid_payment_amount = "Số tiền phải nằm trong khoảng từ {min_amount} đến {max_amount} VND."
error_vietqr_generation_failed = "Không thể tạo mã QR VietQR. Vui lòng thử lại."
menu_cancelled = "Đã hủy tác vụ thành công."

# General error messages
fatal_conversation_exception = "Đã xảy ra lỗi. Vui lòng liên hệ bộ phận hỗ trợ."

# Thanh toán: số tiền thẻ tín dụng
payment_cc_amount = "Bạn muốn thêm bao nhiêu tiền vào ví của mình?\n" \
                    "<i>Chọn một số tiền bằng cách nhấn vào các nút bên dưới, hoặc nhập số tiền trực tiếp.</i>"

# Thành công: sản phẩm đã được xóa
success_product_deleted = "✅ Sản phẩm đã được xóa thành công!"

# Xác nhận thăng cấp quản trị viên
conversation_confirm_admin_promotion = "Bạn có chắc chắn muốn thăng cấp người dùng này thành 💼 Quản lý không?\n" \
                                       "Hành động này không thể hoàn tác!"

# Thuộc tính của quản trị viên
admin_properties = "<b>Quyền hạn của {name}:</b>"

# Quản trị viên: có thể chỉnh sửa sản phẩm?
prop_edit_products = "Chỉnh sửa sản phẩm"

# Quản trị viên: có thể nhận đơn hàng?
prop_receive_orders = "Nhận đơn hàng"

# Quản trị viên: có thể tạo giao dịch?
prop_create_transactions = "Quản lý giao dịch"

# Quản trị viên: hiển thị trong trợ giúp
prop_display_on_help = "Hiển thị cho khách hàng"

# Quản trị viên: Chọn người dùng để chỉnh sửa
conversation_admin_select_user = "Chọn một người dùng để chỉnh sửa."

# Quản trị viên: chọn sản phẩm để chỉnh sửa
conversation_admin_select_product = "✏️ Bạn muốn chỉnh sửa sản phẩm nào?"

# Quản trị viên: chọn sản phẩm để xóa
conversation_admin_select_product_to_delete = "❌ Bạn muốn xóa sản phẩm nào?"

# Chuyển sang chế độ người dùng
conversation_switch_to_user_mode = "Bạn đang chuyển sang chế độ 👤 Khách hàng.\n" \
                                   "Nếu muốn quay lại menu 💼 Quản lý, hãy bắt đầu lại cuộc trò chuyện với lệnh /start."

# Mở menu trợ giúp
conversation_open_help_menu = "Bạn cần loại trợ giúp nào?"

# Hướng dẫn
menu_guide = "📖 Hướng dẫn"

# Tin nhắn trợ giúp
help_msg = "Hướng dẫn sử dụng 3be-telegram có sẵn tại địa chỉ sau:\n" \
           "https://github.com/Steffo99/greed/wiki"

# Thông tin về bot
bot_info = "Bot này đang sử dụng <a href=\"https://github.com/Steffo99/greed\">3be-telegram</a>, " \
           "một framework của @Steffo dành cho thanh toán trên Telegram, được phát hành " \
           "dưới <a href=\"https://github.com/Steffo99/greed/blob/master/LICENSE.txt\">Giấy phép Affero General Public License 3.0</a>."

# Hỏi số tiền để thay đổi số dư
ask_credit = "Bạn muốn thay đổi số dư của khách hàng như thế nào?\n" \
             "\n" \
             "<i>Gửi tin nhắn chứa số tiền.\n" \
             "Dùng dấu </i><code>+</code><i> để cộng tiền, hoặc dấu </i><code>-</code><i> để trừ tiền.</i>"

# Chế độ đơn hàng trực tiếp: Bắt đầu
conversation_live_orders_start = "Bạn đang ở chế độ <b>Đơn hàng trực tiếp</b>\n" \
                                 "Tất cả các đơn hàng mới của khách hàng sẽ xuất hiện trong thời gian thực ở cuộc trò chuyện này.\n" \
                                 "Bạn có thể đánh dấu ✅ Hoàn thành hoặc ✴️ Hoàn tiền cho khách hàng."

# Chế độ đơn hàng trực tiếp: Dừng nhận thông báo
conversation_live_orders_stop = "<i>Nhấn nút Dừng bên dưới để dừng nhận thông báo đơn hàng trực tiếp.</i>"

# Thông báo
notification_order_placed = "Đơn hàng mới đã được tạo:\n" \
                            "{order}"
notification_order_completed = "Đơn hàng của bạn đã được hoàn thành!\n" \
                               "{order}"
notification_order_refunded = "Đơn hàng của bạn đã được hoàn tiền!\n" \
                              "{order}"

emoji_completed = "✅"  # Biểu tượng cho trạng thái đã hoàn thành
text_completed = "Đơn hàng của bạn đã được hoàn tất."  # Văn bản cho trạng thái đã hoàn thành
conversation_cart_actions = "Bạn muốn làm gì với giỏ hàng của mình?"  # Câu hỏi cho hành động giỏ hàng
emoji_not_processed = "❌"  # Biểu tượng cho trạng thái chưa xử lý
text_not_processed = "Đơn hàng này vẫn chưa được xử lý."  # Văn bản cho trạng thái chưa xử lý
ask_refund_reason = "Vui lòng cung cấp lý do hoàn tiền:"  # Yêu cầu lý do hoàn tiền
emoji_refunded = "💵"  # Biểu tượng cho trạng thái đã hoàn tiền
text_refunded = "Đơn hàng này đã được hoàn tiền."  # Văn bản cho trạng thái đã hoàn tiền
refund_reason = "Lý do hoàn tiền: {reason}"  # Hiển thị lý do hoàn tiền
success_order_refunded = "Đơn hàng đã được hoàn tiền thành công."  # Thông báo thành công khi hoàn tiền


# Chuỗi liên quan đến thanh toán
payment_invoice_label = "Thanh toán"
payment_invoice_fee_label = "Phí giao dịch"
payment_invoice_title = "Nạp tiền"
payment_invoice_description = "Nạp số tiền {amount} vào ví của bạn."

# Emoji
emoji_yes = "✅"
emoji_no = "🚫"

# Lỗi
error_nonprivate_chat = "⚠️ Bot này chỉ hoạt động trong cuộc trò chuyện riêng tư."
error_no_orders = "⚠️ Bạn chưa đặt đơn hàng nào nên không có gì để hiển thị."
error_not_enough_credit = "⚠️ Bạn không có đủ tiền để đặt đơn hàng."

# Thành công
success_product_edited = "✅ Sản phẩm đã được thêm/chỉnh sửa thành công!"
success_order_created = "✅ Đơn hàng đã được tạo thành công!\n{order}"
