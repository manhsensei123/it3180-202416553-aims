# Câu hỏi thảo luận Lab 03

1. **Merge base là gì?**
   - Merge base là commit tổ tiên chung gần nhất (common ancestor) của hai nhánh khi thực hiện gộp (merge). Git thực hiện three-way merge bằng cách so sánh trạng thái tại merge base với đầu mút của hai nhánh: nếu chỉ một bên sửa thì Git tự động gộp, còn nếu cả hai nhánh cùng sửa một vùng mã nguồn khác nhau so với merge base thì sẽ phát sinh xung đột (merge conflict).

2. **Vì sao trên `master` và `release/*` bắt buộc phải dùng `git revert` thay vì `git reset`?**
   - `master` và `release/*` là các nhánh lịch sử chung đã chia sẻ cho cả nhóm và bị khóa bảo vệ chống force-push. Dùng `git reset` sẽ xóa bỏ commit và viết lại lịch sử, làm lệch nhánh của tất cả thành viên khác. Ngược lại, `git revert` tạo ra một commit mới có nội dung đảo ngược thay đổi cũ, vừa khôi phục mã nguồn an toàn vừa giữ nguyên dấu vết kiểm toán (audit trail) trong SCM.
