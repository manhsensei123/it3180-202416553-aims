# Câu hỏi thảo luận Lab 01

1. **Cấu hình `--global` lưu ở đâu và khác gì `--local`?**
   - `--global` lưu trong tệp `~/.gitconfig` của người dùng, áp dụng cho mọi kho Git trên máy.
   - `--local` lưu trong `.git/config` của riêng kho hiện tại và được ưu tiên cao hơn `--global`.

2. **Vì sao dùng `git mv` thay vì xóa rồi tạo lại tệp?**
   - Giúp Git nhận diện thao tác đổi tên/di chuyển tệp ngay trên vùng staging và bảo toàn lịch sử thay đổi xuyên suốt khi tra cứu bằng `git log --follow`.

3. **Nhánh `release/lab01` có phải là một baseline không?**
   - Có. Đây là phiên bản cấu hình đã hoàn chỉnh, thống nhất tại thời điểm kết thúc Lab 01 để làm mốc nộp bài, không sửa đổi trực tiếp tùy tiện.

4. **Vì sao không commit thẳng lên `master` dù làm một mình?**
   - Để giữ `master` luôn ở trạng thái ổn định, tách biệt các thay đổi đang làm dở sang nhánh riêng và rèn quy trình kiểm tra lại thay đổi qua Pull Request trước khi tích hợp.
