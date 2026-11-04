# Câu hỏi thảo luận Lab 02

1. **Vì sao phải đồng bộ `master` vào nhánh tính năng trước khi gửi PR?**
   - Vì trong lúc phát triển song song, `master` có thể đã nhận thêm thay đổi mới từ nhánh khác. Đồng bộ trước giúp phát hiện xung đột và chạy kiểm thử tích hợp ngay trên nhánh riêng, đảm bảo mã sau khi merge vào `master` hoạt động ổn định.

2. **Khi nào KHÔNG được dùng `rebase`?**
   - Tuyệt đối không dùng `rebase` trên các nhánh dùng chung đã chia sẻ công khai (như `master`, `release/*`), vì `rebase` viết lại lịch sử và tạo mã SHA mới, gây lệch lịch sử nghiêm trọng cho những người khác đang làm việc trên nhánh đó.

3. **Nhánh `feature/*` khác `topic/*` ra sao?**
   - `feature/*` dùng để phát triển các chức năng nghiệp vụ của sản phẩm phục vụ người dùng (như in giỏ hàng, tìm kiếm đĩa).
   - `topic/*` dùng cho các công việc phụ trợ, tài liệu, cấu hình kho hoặc quy trình kỹ thuật (như thêm PR template, sơ đồ Use Case, cấu hình CI).
